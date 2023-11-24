import matplotlib.pyplot as plt
from io import BytesIO
import base64
from fastapi.responses import HTMLResponse

# New endpoint to generate and return a pie chart
@app.get("/chart", response_class=HTMLResponse)
async def get_pie_chart():
    labels = ['A', 'B', 'C', 'D']
    sizes = [15, 30, 45, 10]

    plt.figure(figsize=(6, 6))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')

    img_buf = BytesIO()
    plt.savefig(img_buf, format='png')
    img_buf.seek(0)

    img_base64 = base64.b64encode(img_buf.read()).decode('utf-8')

    plt.close()

    # Create an HTML page that includes the image
    html_content = f"<img src='data:image/png;base64,{img_base64}'/>"
    
    return HTMLResponse(content=html_content)
