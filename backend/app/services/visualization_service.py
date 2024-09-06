'''import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import plotly.express as px
from io import BytesIO
import base64

class VisualizationService:
    """
    Service for creating visualizations from SEO data.
    """

    def __init__(self):
        pass

    def visualize_keyword_trends(self, transformed_data: pd.DataFrame) -> str:
        """
        Create a line chart visualizing keyword trends over time.

        :param transformed_data: The DataFrame containing SEO data.
        :return: Base64 string of the generated image.
        """
        fig = px.line(transformed_data, x='Date', y='Keyword Density', color='Keyword',
                      title='Keyword Trends Over Time')
        return self._save_plot_to_base64(fig)

    def visualize_competitor_comparison(self, transformed_data: pd.DataFrame) -> str:
        """
        Create a bar chart comparing SEO metrics of competitors.

        :param transformed_data: The DataFrame containing SEO data.
        :return: Base64 string of the generated image.
        """
        fig = px.bar(transformed_data, x='Competitor', y='SEO Score', color='Keyword',
                     title='Competitor SEO Comparison')
        return self._save_plot_to_base64(fig)

    def _save_plot_to_base64(self, fig) -> str:
        """
        Save the current Plotly plot as a base64 string.

        :param fig: The Plotly figure to save.
        :return: Base64 encoded string of the plot image.
        """
        image_base64 = base64.b64encode(fig.to_image(format="png")).decode('utf-8')
        return image_base64

'''
