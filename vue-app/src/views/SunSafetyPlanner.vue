<template>

<div class="banner" style="text-align: left;">
    <h1>Your Personalised Sun Safety Plan</h1>
    <h3>Tailored sun safety recommendations based on your skin type.</h3>
</div>
<div class="header" style="text-align: left;">
    <h1>Input your skin type</h1>
    <h3>Please input your skin type for personalised recommendations</h3>
    
    <div style="display: flex; justify-content: center;">
        <div class="skin-chart">
            <container style="text-align: center;">
                <div class="circle" style="background-color: rgb(231,205,184);"></div>
                <h2>Type I</h2>
            </container>
            <container style="text-align: center;">
                <div class="circle" style="background-color: rgb(228,182,150);"></div>
                <h2>Type II</h2>
            </container>
            <container style="text-align: center;">
                <div class="circle" style="background-color: rgb(221,178,119);"></div>
                <h2>Type III</h2>
            </container>
            <container style="text-align: center;">
                <div class="circle" style="background-color: rgb(194,134,88);"></div>
                <h2>Type IV</h2>
            </container>
            <container style="text-align: center;">
                <div class="circle" style="background-color: rgb(141,99,56);"></div>
                <h2>Type V</h2>
            </container>
            <container style="text-align: center;">
                <div class="circle" style="background-color: rgb(116,74,50);"></div>
                <h2>Type VI</h2>
            </container>
        </div>
    </div>

    <div style="margin-top: 15%;">
        <input type="file" name="image" accept="image/jpeg,image/x-png,image/gif" @change="uploadFile">
        <button @click="submitImg" style="background-color: black; color: white; width:120px; height: 50px;">Analyse skin tone</button>
        <div v-if="analysedSkinTone">
            <h2>Your skin tone is {{ analysedSkinTone }}</h2>
        </div>
        <div>
            <h2>Skin tone types:</h2>
            <p>LIGHT = Type I</p>
            <p>MID-LIGHT = Type II and III</p>
            <p>MID-DARK = Type IV and V</p>
            <p>DARK= Type VI</p>
        </div>
    </div>
    <div style="display: flex; align-items: right; justify-content: right;">
        <form @submit.prevent="submitDetails">
            <div style="margin-right: 21%; margin-bottom: 1%;">
                <label for="skinType" class="form-label">Skin Type</label>
            </div>
            <select class="form-select" id="skinType" v-model="userData.skinType">
                <option value="" disabled>Choose your skin type from the chart</option>
                <option value="I">Skin Type I</option>
                <option value="II">Skin Type II</option>
                <option value="III">Skin Type III</option>
                <option value="IV">Skin Type IV</option>
                <option value="V">Skin Type V</option>                    
                <option value="VI">Skin Type VI</option>
            </select>
            <div style="margin-top: 1%; display: flex; justify-content: right;">
                <button type="submit" class="btn btn-primary me-2" style="background-color: black; color: white;">Submit</button>
            </div>
            <div style="margin-top: 1%; display: flex; justify-content: right;">
                <button type="button" class="btn btn-secondary" style="background-color: black; color: white;" @click="clearForm">Clear</button>
            </div>
        </form>
    </div>
</div>

<div v-if="submittedForm" style="font-size: smaller; width: 600px; margin: auto;">
    <h1>Your Personalised Sun Protection Plan and Specific UV Risks</h1>

    <div>
        <h2 style="font-size: 30px;">Sunscreen SPF Levels</h2>
        <h2 style="color: gray;">Based on current U.V index</h2>
        <div class="answer-form">
            <h1>SPF 50+</h1> 
        </div>
    </div>

    <div>
        <h2 style="font-size: 30px;">Recommended time to spend in the sun without risk of burning</h2>
        <h2 style="color: gray;">Curated for your skin tone in order to maintain optimal vitamin D levels</h2>
        <div class="answer-form">
            <h1 v-if="submittedType">{{ skinTypeTime[submittedType] }}</h1>
        </div>
    </div>

</div>

<div style="font-size: smaller; width: 600px; margin: auto; margin-top: 15%; margin-bottom: 5%;">
    <h1>Benefits of Sun Exposure</h1>
</div>
<div style="justify-content: center; gap: 100px; display: flex;">
    <a href="https://healthybonesaustralia.org.au/your-bone-health/vitamin-d-bone-health/">
        <div class="card">
            <div class="image-holder">
                <img src="/vitd.webp" class="img-fluid" alt="Vitamin D importance" style="height: auto; width: 150px;"/>
            </div>
            <div class="text-desc">
                <h2>Vitamin D & Bone Health</h2>
                <h3>Vitamin D is a crucial requirement for various health reasons. Find out how in this article.</h3>
            </div>
        </div>
    </a>

    <a href="https://www.healthdirect.gov.au/vitamin-d-deficiency">
        <div class="card">
            <div class="image-holder">
                <img src="/vitdicon.jpg" class="img-fluid" alt="vitamin D deficiency" style="height: auto; width: 150px;"/>
            </div>
            <div class="text-desc">
                <h2>Vitamin D deficiency</h2>
                <h3>This article goes further into detail about vitamin D deficiency and its symptoms.</h3>
            </div>
        </div>
    </a>

    <a href="https://www.mssociety.org.uk/research/latest-research/latest-research-news-and-blogs/new-insights-role-vitamin-d-our-immune-system">
        <div class="card">
            <div class="image-holder">
                <img src="/sunshine.jpg" class="img-fluid" alt="hat" style="height: auto; width: 160px;"/>
            </div>
            <div class="text-desc">
                <h2>New insights into the role of vitamin D in our immune system</h2>
                <h3>Vitamin D found to be linked to a reduced immune response.</h3>
            </div>
        </div>
    </a>
</div>


</template>


<script setup>
import { ref } from 'vue';

const uploadedFile = ref(null);
const analysedSkinTone = ref(null);

const userData = ref({
    skinType:'',

});

const submittedDetails = ref([]);

const submittedType = ref('');
const submittedForm = ref(false);

const submitDetails = () => {
    if(!errorInput.value.skinType){
        submittedDetails.value.push({...userData.value});
        submittedForm.value = true;
        submittedType.value = userData.value.skinType;
        clearForm();
    }
};

const clearForm = () => {
    userData.value = {
        skinType: ''
    };
};

const errorInput = ref({
    skinType: null
});

const skinTypeTime = { 
    "I": "10-15m",
    "II": "15-20m",
    "III": "20-30m",
    "IV": "30-40m",
    "V": "40-60m",
    "VI": "60-80m"
}

const uploadFile = (fileuploaded) => {
    uploadedFile.value = fileuploaded.target.files[0];
}

const submitImg = async() => {
    const formData = new FormData();
    formData.append("image", uploadFile.value);
}






</script>


<style scoped>
.banner{
    background-color: rgb(103, 202, 248);
    color: white;
    text-align: center;
    padding: 50px;
    font-size: 16px;
    font-weight: bold;
}

.header{
    padding: 50px;
    font-size: 13px;
    font-weight: bold;
    margin-top: 6%; 
    /* background-color: aqua; */
}

.form-select{
    width: 280px;
    height: 30px;
}

.form-label{
    font-size: larger;
}

.skin-chart{
    height: 150px;
    width: 650px;
    display: flex;
    align-items: center;
    justify-content: center;
    margin-top: 3%;
}

.circle{
    width: 100px;
    height: 100px;
    border-radius: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
}

.answer-form{
    background-color: #f1f1f1;
    width: 600px;
    height: 100px;
}

.text-desc{
    text-align: center;
    color: black;
}

.card{
    background-color: white;
    width: 250px;
    height: 400px;
    display: flex; flex-direction: column;
    align-items: center;
    justify-content: center;
    border-style:solid;
    border-color: #f1f1f1;
    margin-left: auto;
}

.image-holder{
    /* background-color: #f1f1f1; */
    width: 240px;
    height: 400px;
    display: flex;
    align-items: center;
    justify-content: center;
}


</style>