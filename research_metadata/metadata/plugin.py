import pluggy

hookspec = pluggy.HookspecMarker("metadata")
hookimpl = pluggy.HookimplMarker("metadata")

class MySpec:
    """A hook specification namespace."""

    @hookspec
    def generate_readme(metadata):
        """Generate README.txt based on the metadata"""

class MetadataPlugin:
    """A hook implementation namespace."""

    @hookimpl
    def generate_readme(self, metadata):
        dublin_core_template = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta name="DC.title" content="Research Metadata">
            <meta name="DC.creator" content="{metadata.data_provider}">
            <meta name="DC.format" content="{metadata.data_format}">
            <meta name="DC.description" content="{metadata.degree_of_aggregation}">
        </head>
        <body>
            <h1>Research Metadata</h1>
            <p>Data Provider: {metadata.data_provider}</p>
            <p>Data Format: {metadata.data_format}</p>
            <p>Degree of Aggregation: {metadata.degree_of_aggregation}</p>
        </body>
        </html>
        
        """
        with open("README.txt", "w") as readme_file:
            readme_file.write(dublin_core_template)


