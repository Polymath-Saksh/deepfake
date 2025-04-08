# DeepFake-Analysis ![Hugging Face](https://img.shields.io/badge/Hugging%20Face-FFD21E?logo=huggingface&logoColor=000) ![Django](https://img.shields.io/badge/Django-%23092E20.svg?logo=django&logoColor=white) ![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff) 

## Introduction

This repository contains the AI Ambassadors Project of Microsoft Learn Student Ambassadors. The project is about DeepFake Image Detection Model. The project is divided into two parts:

### Development of a DeepFake Image Detection Model

- Inspired by "[An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale](https://arxiv.org/abs/2010.11929)" by Dosovitskiy et al. (2020) The concerned Vision Transformer model is used for transfer learning on the DeepFake Detection Dataset.

- A subset of Open Forensics Dataset ([Deepfake Dataset](https://www.kaggle.com/datasets/manjilkarki/deepfake-and-real-images/data)) consisting of approx. 1.9 million images is used for training the model. The dataset is divided into 3 sets: Training, Validation, and Testing Sets with a 14:4:1 ratio. Thereby, making the use of Transfer Learning for training the model to work on detecting DeepFake Images.

- The model trained is then deployed onto Hugging Face Model Hub for public use. The model is available for use at: [DeepFake Image Detection Model](https://huggingface.co/sakshamkr1/deepfake_vit)

## Model Statistics

- Achieved an accuracy of 97% on the Testing Set.
- Model trained on Azure ML Studio notebooks, with a compute VM of 16 Core, 128 GB RAM for a period of 6 hours.
- The model is available for use at: [DeepFake Image Detection Model](https://huggingface.co/sakshamkr1/deepfake_vit)

## Web Application

- The Web Application is developed using Django Framework.
- The Web Application retrieves the image from the user via a user-friendly interface. During deployment, the model is retrieved from the Hugging Face Model Hub via the API, hence the user does not need to download the model in the concerned project directory.
- The Web Application can be further deployed on Azure App Services for public use.

## App Demo

https://github.com/user-attachments/assets/d0e1601f-dccd-42a8-9f63-18964702114f

## Presentation

The presentation for the project can be found at: [Team DeepShield - Deepfake Analysis Presentation](https://stdntpartners-my.sharepoint.com/:p:/g/personal/saksham_kumar_studentambassadors_com/EbQveM3-pCVDtwFR2JevNJ0BP2wviEIPJQd5CHQK6RHJ2A?e=fYrmRQ).

Access restricted to Microsoft Learn Student Ambassadors.

## Installation and Usage

- Clone the repository using the following command:

    ```bash
    git clone https://github.com/Polymath-Saksh/deepfake.git
    ```

- Install the required dependencies using the following command:

    ```bash
    pip install -r requirements.txt
    ```

- Run the Django Server using the following command:

    ```bash
    python manage.py runserver
    ```

## Contributors

- [Rhythm Narang](https://github.com/rhythmnarang1)
- [Saksham Kumar](https://github.com/Polymath-Saksh)

## Acknowledgements

- [Dmytro Lakubovskyi](https://www.kaggle.com/dima806)'s Kaggle for ideas on the Vision Transformer Model and Deepfake Model Development.

- [An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale](https://arxiv.org/abs/2010.11929) by Dosovitskiy et al. (2020) for the Vision Transformer Model.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
