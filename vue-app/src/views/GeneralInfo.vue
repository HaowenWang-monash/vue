<template>
<div class="banner">
    <h1>Understanding UV Radiation in Australia</h1>
    <h3>Tailored sun safety recommendations based on your skin type.</h3>
</div>
<div class="header">
    <h1>General Information on UV Dangers</h1>
    <h3>Learn about the risks associated with UV radiation in Australia</h3>
</div>

<div class="header" style="display: flex;flex-wrap: wrap; justify-content: center; margin-top: 0%; gap: 2%;">
    <div class="article-holder">
        <a href="https://www.arpansa.gov.au/understanding-radiation/what-is-radiation/non-ionising-radiation/ultraviolet-radiation#:~:text=Sun%20exposure%20causes%20the%20outer,UVR%20at%20an%20early%20age.">
            <div class="text-content">
                <h2>UV Basics</h2>
                <h3>UV radiation comes from the sun and damages the skin leading to various health issues.</h3>
            </div>
        </a>
    </div>
    <div class="article-holder">
        <a href="https://www.cancer.org.au/cancercareguides/basal-and-squamous-cell-carcinoma?gad_source=1&gclid=Cj0KCQjw7dm-BhCoARIsALFk4v81i3cKP3SOu_zeOpa81nqnV9Kel4VpTwnYLTdA9nJ6KmbVHblAUDMaApabEALw_wcB">
            <div class="text-content">
                <h2>Skin Cancer Risk</h2>
                <h3>Australia has one of the highest rates of skin cancer due to high UV levels.</h3>
            </div>
        </a>
    </div>
    <div class="article-holder" style="margin-top: 2%;">
        <a href="https://www.stevekmd.com/blog/5-eye-conditions-caused-by-sun-damage">
            <div class="text-content">
                <h2>Eye Damage</h2>
                <h3>UV exposure can also harm your eyes and lead to vision problems.</h3>
            </div>
        </a>
    </div>
</div>

<div class="header" style="margin-top: 0%;">
    <h1>Skin Cancer rates in Australia</h1>
    <h3>A quick visualisation of skin cancer rates according to each state in Australia</h3>

    <div style="margin-top: 3%;">
        <iframe src="http://127.0.0.1:8050/" style="width: 800px; height: 600px;"></iframe>
    </div>
</div>
<div class="header" style="margin-top: 0%;">
    <h1>Skin Cancer rates in Australia</h1>
    <h3>A quick visualisation of skin cancer rates according to each state in Australia</h3>

    <div style="margin-top: 3%;">
        <img src="/datagraph.png" class="img-fluid" alt="Vitamin D importance" style="width: 700px; height: 400px;"/>
    </div>
</div>

<div class="header">
    <h1>Understanding the U.V Index</h1>
    <h3>A guide to interpreting UV Index levels and their effects on health</h3>
</div>

<div class="header" style="display: flex;flex-wrap: wrap; justify-content: center; margin-top: 0%; gap: 2%;">
    <div class="article-holder-2">
        <div class="text-content">
            <h3 style="color: gray;">Low U.V index</h3>
            <h2>0-2</h2>
            <h3>Low risk of harm</h3>
        </div>
    </div>
    <div class="article-holder-2">
        <div class="text-content">
            <h3 style="color: gray;">Moderate U.V index</h3>
            <h2>3-5</h2>
            <h3>Take precautions!</h3>
        </div>
    </div>
    <div class="article-holder-2">
        <div class="text-content">
            <h3 style="color: gray;">High U.V index</h3>
            <h2>6-7</h2>
            <h3>Risk of harm, ensure to protect yourself</h3>
        </div>
    </div>
    <div class="article-holder-2">
        <div class="text-content">
            <h3 style="color: gray;">Very high U.V index</h3>
            <h2>8-10</h2>
            <h3>Be extra cautious</h3>
        </div>
    </div>
    <div class="article-holder-2">
        <div class="text-content">
            <h3 style="color: gray;">Extreme U.V index</h3>
            <h2>11+</h2>
            <h3>Dangerous levels, avoid outdoor activity</h3>
        </div>
    </div>


</div>

</template>


<script>


</script>


<style>
.banner{
    background-color: rgb(103, 202, 248);
    color: white;
    text-align: left;
    padding: 50px;
    font-size: 14px;
    font-weight: bold;
    color: black;
}

.header{
    padding: 50px;
    font-size: 13px;
    font-weight: bold;
    margin-top: 6%; 
    /* background-color: aqua; */
}

.article-holder{
    width: 40%;
    height: 150px;
    display:flex;
    border-style:solid;
    border-color: #f1f1f1;
    text-align:left;
}

.text-content{
    margin-left: 2%;
}

.article-holder-2{
    width: 30%;
    height: 150px;
    display:flex;
    border-style:solid;
    border-color: #f1f1f1;
    text-align:left;
}

</style>