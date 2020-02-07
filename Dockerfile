# Docker file for the Online Shopping Intention Predictor 
# Team 309, Feb, 2020

# use rocker/tidyverse as the base image and
FROM rocker/tidyverse

# install some R packages
RUN apt-get update -qq && apt-get -y --no-install-recommends install \
  && install2.r --error \
    --deps TRUE \
    here \
    caret \
	docopt

# install other R packages using install.packages
RUN Rscript -e "install.packages('kableExtra')"
RUN Rscript -e "install.packages('gridExtra')"
RUN Rscript -e "install.packages('plotly')"
RUN Rscript -e "install.packages('cowplot')"
RUN Rscript -e "install.packages('pheatmap')"


# install the anaconda distribution of python
RUN wget --quiet https://repo.anaconda.com/archive/Anaconda3-2019.10-Linux-x86_64.sh -O ~/anaconda.sh && \
    /bin/bash ~/anaconda.sh -b -p /opt/conda && \
    rm ~/anaconda.sh && \
    ln -s /opt/conda/etc/profile.d/conda.sh /etc/profile.d/conda.sh && \
    echo ". /opt/conda/etc/profile.d/conda.sh" >> ~/.bashrc && \
    echo "conda activate base" >> ~/.bashrc && \
    find /opt/conda/ -follow -type f -name '*.a' -delete && \
    find /opt/conda/ -follow -type f -name '*.js.map' -delete && \
    /opt/conda/bin/conda clean -afy && \
    /opt/conda/bin/conda update -n base -c defaults conda

# put anaconda python in path
ENV PATH="/opt/conda/bin:${PATH}"

# install python packages
RUN conda install -c conda-forge lightgbm 
RUN	conda install -c anaconda docopt  
RUN /opt/conda/bin/conda install -y anaconda numpy
RUN /opt/conda/bin/conda install -y anaconda pandas
RUN conda install -c jmcmurray os -y
RUN pip install -U scikit-learn

CMD ["/bin/bash"]







