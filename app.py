from flask import Flask, render_template, request
import math

app = Flask(__name__)

def regresi(xs, ys):
    n = len(xs)
    xm, ym = sum(xs)/n, sum(ys)/n
    sxx = sum((x-xm)**2 for x in xs)
    syy = sum((y-ym)**2 for y in ys)
    sxy = sum((x-xm)*(y-ym) for x,y in zip(xs,ys))
    if sxx == 0:
        raise ValueError("Semua konsentrasi standar tidak boleh sama.")
    slope = sxy/sxx
    intercept = ym-slope*xm
    r = sxy/math.sqrt(sxx*syy) if syy else 0.0
    return r, slope, intercept

@app.route("/", methods=["GET", "POST"])
def index():
    result = error = None
    standards = [{"x":"","y":""} for _ in range(5)]
    sample_response = ""
    if request.method == "POST":
        try:
            xr = request.form.getlist("concentration[]")
            yr = request.form.getlist("response[]")
            standards = [{"x":x.strip(),"y":y.strip()} for x,y in zip(xr,yr)]
            sample_response = request.form.get("sample_response","").strip()
            pairs = []
            for x,y in zip(xr,yr):
                if not x.strip() and not y.strip(): continue
                if not x.strip() or not y.strip():
                    raise ValueError("Setiap baris standar harus memiliki konsentrasi dan respons.")
                pairs.append((float(x),float(y)))
            if len(pairs) < 3:
                raise ValueError("Masukkan minimal 3 titik standar lengkap.")
            xs,ys = [p[0] for p in pairs],[p[1] for p in pairs]
            r,slope,intercept = regresi(xs,ys)
            conc = None
            if sample_response:
                if slope == 0: raise ValueError("Slope nol; konsentrasi sampel tidak dapat dihitung.")
                conc = (float(sample_response)-intercept)/slope
            result = dict(n=len(pairs),r=r,slope=slope,intercept=intercept,conc=conc,
                          equation=f"y = {slope:.8g}x {'+' if intercept >= 0 else '−'} {abs(intercept):.8g}")
        except ValueError as e:
            error = str(e)
        except Exception:
            error = "Data tidak dapat diproses. Periksa kembali angka yang dimasukkan."
    return render_template("index.html", result=result, error=error, standards=standards, sample_response=sample_response)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000, debug=True)
