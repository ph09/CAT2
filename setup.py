from setuptools import setup

setup(
    name='cat',
    version='2.0',
    packages=['cat', 'tools'],
    python_requires='>=3.7.0',
    install_requires=[
        'pyfasta>=0.5.2',
        'toil>=8.0',
        'luigi>=3.5',
        'seaborn>=0.13.1',
        'pandas>=2.2.2',
        'frozendict==2.4.6',
        'configobj>=5.0',
        'sqlalchemy>=1.3.15',
        'ete3>=3.0',
        'pysam>=0.19.1',
        'numpy>=1.20.0',
        'scipy>=1.13',
        'bx-python>=0.12',
        'gffutils>=0.10',
        'biopython>=1.76'
    ],
    scripts=['programs/cat_to_ncbi_submit', 'programs/translate_gene_pred',
             'programs/validate_gff3', 'programs/cat_parse_ncbi_genbank',
             'programs/cat_parse_ncbi_refseq', 'programs/cat_parse_prokka_gff3'],
    author='Ian Fiddes, Prajna Hebbar',
    description='Comparative Annotation Toolkit',
    url='https://github.com/ComparativeGenomicsToolkit/Comparative-Annotation-Toolkit',
    license='Apache 2.0',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Bioinformatics',
        'Topic :: Bioinformatics',
        'License :: Apache 2.0',
        'Programming Language :: Python :: 3.7'
    ],
    keywords='bioinformatics comparative genomics',
)
