import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from quadratic_solver import QuadraticSolver

def find_graph_range(equation_roots: list) -> list:
    """Function to get the X-Axis range"""

    graph_range = []
    roots_len = len(equation_roots)

    match roots_len:
        case 0:
            graph_range = [-10, 10]

        case 1:
            root_round = round(equation_roots[0], 0)
            graph_range = [-(abs(root_round) + 5), abs(root_round) + 5]

        case 2:
            max_root = equation_roots[0]
            if (abs(max_root) < abs(equation_roots[1])):
                max_root = equation_roots[1]

            root_round = round(max_root, 0)
            graph_range = [-(abs(root_round) + 5), abs(root_round) + 5]

    return graph_range

#CSS
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)

#Header
with st.container():
    st.title("Quick Quadratic")

    st.latex("ax^2 + bx + c = 0")

    st.markdown("---")

#Body
col1, col2 = st.columns(2)

col1.write("## Coefficient Values")

a_value = col1.slider(label="Coefficient a", min_value=-10.0, max_value=10.0, step=0.1, value=-0.2)
b_value = col1.slider(label="Coefficient b", min_value=-10.0, max_value=10.0, step=0.1, value=-3.7)
c_value = col1.slider(label="Coefficient c", min_value=-10.0, max_value=10.0, step=0.1, value=0.8)

quad_solver = QuadraticSolver(a_value, b_value, c_value)

with col2:
    st.write("## Your Equation")

    st.latex(f"{a_value}x^2 + {b_value}x + {c_value} = 0")

    roots = quad_solver.find_roots()

    if len(roots) == 0:
        st.write(f"The equation has no real roots")

    elif len(roots) == 1:
        st.write("Root of the equation :")
        st.write(f"({roots[0]})")

    else:
        st.write("Roots of the equation :")
        st.write(f"({roots[0]}, {roots[1]})")

x_range = find_graph_range(roots)
y_range = [-20, 20]

x_y_values = quad_solver.get_plot_values()

chart_data = pd.DataFrame(x_y_values)

fig = px.line(chart_data, x="x", y="y")

fig.update_xaxes(type="linear", range=x_range, showgrid=True,gridwidth=0.2,
        gridcolor='Gray', zeroline=True, zerolinewidth=3, zerolinecolor='LightPink')

fig.update_yaxes(type="linear", range=y_range, showgrid=True,gridwidth=0.2,
        gridcolor='Gray', zeroline=True, zerolinewidth=3, zerolinecolor='LightPink')

if len(roots) > 0:
    fig.add_trace(go.Scatter(x=[roots[0]], y=[0], mode = 'markers',
                            marker_symbol = 'circle',
                            marker_size = 15))
    if len(roots) == 2:
        fig.add_trace(go.Scatter(x=[roots[1]], y=[0], mode = 'markers',
                                marker_symbol = 'circle',
                                marker_size = 15))

fig.for_each_trace(lambda t: t.update(name = "root"))

st.plotly_chart(fig)

#Footer
st.markdown("---")

st.markdown(
    "More infos and :star: at [github.com/kunaldhanwaria/QuickQuadratic](https://github.com/kunaldhanwaria/QuickQuadratic)"
)
