<div>
<h1>VideoMaker Rest API</h1>
<p>Django Rest framework VideoMaker API, which will help users to Create/Read/Update/Delete Video Audio elements</p>

<h4>Sample Output</h4>
<strong><a href='https://rst-api.herokuapp.com/Api/'>live hosted on heroku</a></strong>

<br>

```console
{
    "id": 1,
    "typee": "bg_music",
    "high_volume": 50,
    "low_volume": 40,
    "video_component_id": "qwerty",
    "url": "https://rst-api.herokuapp.com/Api/VideoMaker/",
    "duration": {
        "id": 1,
        "start_time": 20,
        "end_time": 40
    }
}
```
<hr></hr>

<h3>Requirments</h3>
<ul>
    <li>Python 3.11.3</li>
    <li>Django 4.2.1</li>
    <li>Django Rest Framework</li>
</ul>


<h3>Installation</h3>
<p><code>git clone https://github.com/Roshan-Here/Audio-Element-Rest-API</code></p>
<p>Create virtual environment (<a href="https://docs.conda.io/en/latest/">I'm Using Conda</a>)
</p>

<h5 align='center'>Run Locally</h5>

```console
pip install -r requirements.txt
cd AudioElement
python manage.py makemigrations
python manage.py runserver
```

<h4>Commands</h4>

```console
To fetch all Datas:
https://rst-api.herokuapp.com/Api/VideoMaker/all

To Create Audio Element:
https://rst-api.herokuapp.com/Api/VideoMaker/

To View Audio Element with id:
https://rst-api.herokuapp.com/Api/VideoMaker/{id}

To Update Audio Element:

https://rst-api.herokuapp.com/Api/VideoMaker/{id}/update

To Delete Audio Element:
https://rst-api.herokuapp.com/Api/VideoMaker/{id}/delete


```
</div>

<div>
<h2>Sample Output <a href='https://rst-api.herokuapp.com/Api/VideoMaker/'>live</a></h2
>


<h4>Create View</h4>
<img src="SampleOutput/sample 2.png" alt="" srcset="">


<h4>Main Api View</h4>
<img src="SampleOutput/sample 1.png" alt="" srcset="">

<h4>Detail View</h4>
<img src="SampleOutput/sample 3.png" alt="" srcset="">

<h4>Update View</h4>
<img src="SampleOutput/sample 4.png" alt="" srcset="">

<h4>Delete View</h4>
<img src="SampleOutput/sample 5.png" alt="" srcset="">

</div>

<h3><a href="https://github.com/Roshan-Here/Audio-Element-Rest-API/blob/main/LICENSE">License</a></h3>