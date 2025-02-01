# 🩺 Pneumonia Detection Using CNN  

## 📌 Project Overview  
Pneumonia is a severe lung infection that can be life-threatening if not diagnosed and treated in time. Traditional diagnostic methods, such as chest X-rays analyzed by radiologists, can be time-consuming and subject to human error. With the advancement of deep learning techniques, automated detection using Convolutional Neural Networks (CNNs) has shown promising results in medical image analysis.  

This project aims to develop a **CNN-based model** to classify chest X-ray images as either **PNEUMONIA** or **NORMAL**. The dataset consists of **5,216 labeled images**, which were used to train and evaluate the model. By leveraging deep learning, this study seeks to enhance the accuracy and efficiency of pneumonia diagnosis, potentially aiding healthcare professionals in **early detection and treatment**.  

---

## 📊 Model Performance  
The trained CNN model achieved an **accuracy of 98.01%**, demonstrating strong classification capabilities.  

### 🔍 Confusion Matrix Analysis  
| Prediction | PNEUMONIA | NORMAL |
|------------|-----------|--------|
| **PNEUMONIA (Actual)** | ✅ 1245 | ❌ 96 |
| **NORMAL (Actual)** | ❌ 8 | ✅ 3867 |

### ✨ Key Observations  
✅ The model effectively distinguishes between pneumonia and normal cases.  
⚠️ The false negative rate (FN = 96) is relatively small but important, as misclassification could delay treatment.  
✅ The false positive rate (FP = 8) is very low, reducing unnecessary anxiety and treatment.  

---

## 📂 Dataset  
The dataset used in this project consists of chest X-ray images labeled as **PNEUMONIA** or **NORMAL**. You can access the dataset from the following link:  
📌 [Pneumonia Detection Dataset](https://thecleverprogrammer.com/2020/11/22/pneumonia-detection-with-python/)  

---

## 🚀 Try It Yourself  
You can **test the model in real-time** on Hugging Face! Click the link below to access the **Pneumonia Detection System**:  
🖥️ **Live Demo:** [Pneumonia Detection System on Hugging Face](https://huggingface.co/spaces/Senasu/Pneumonia_Detection_System)  

---
