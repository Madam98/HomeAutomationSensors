

package com.example.myapplication

import retrofit2.converter.gson.GsonConverterFactory
import com.google.gson.GsonBuilder


import android.os.Bundle
import android.util.Log
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity
import retrofit2.Call
import retrofit2.Callback
import retrofit2.Response
import retrofit2.Retrofit
//import retrofit2.converter.moshi.MoshiConverterFactory
import retrofit2.http.GET
import kotlin.reflect.typeOf
import android.os.Handler;
import android.widget.Button


class MainActivity : AppCompatActivity() {


    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        findViewById<Button>(R.id.refreshButton).setOnClickListener{
            //CZYTANIE CO2
            val service = Retrofit.Builder()
                .baseUrl("http://192.168.0.30:8000")
                .addConverterFactory(GsonConverterFactory.create())
                .build()
                .create(CO2Service::class.java)

            service.getCO2().enqueue(object : Callback<CO2> {
                override fun onFailure(call: Call<CO2>, t: Throwable) {
                    Log.d("TAG_", "An error happened!")
                    t.printStackTrace()
                }

                override fun onResponse(call: Call<CO2>, response: Response<CO2>) {
                    Log.d("Call request", call.request().toString())
                    Log.d("Call request header", call.request().headers.toString())
                    Log.d("Response raw header", response.headers().toString())

                    System.out.println(response.body())
                    System.out.println(response.code())

                    response.body()?.let { System.out.println(it.date_time) }
                    findViewById<TextView>(R.id.CO2Value).text = response.body()?.let {it.co_value}.toString() + "\nppm"

                    response.body()?.let { System.out.println(it.co_warning) }
                }
            })


            // CZYTANIE TEMP & HUMIDITY
            val service2 = Retrofit.Builder()
                .baseUrl("http://192.168.0.30:8000")
                .addConverterFactory(GsonConverterFactory.create())
                .build()
                .create(HumTempService::class.java)

            service2.getHumTemp().enqueue(object : Callback<HumTemp> {
                override fun onFailure(call: Call<HumTemp>, t: Throwable) {
                    Log.d("TAG_", "An error happened!")
                    t.printStackTrace()
                }

                override fun onResponse(call: Call<HumTemp>, response: Response<HumTemp>) {
                    Log.d("Call request", call.request().toString())
                    Log.d("Call request header", call.request().headers.toString())
                    Log.d("Response raw header", response.headers().toString())

                    System.out.println(response.body())
                    System.out.println(response.code())

                    response.body()?.let { System.out.println(it.date_time) }
                    findViewById<TextView>(R.id.TempValue).text = response.body()?.let {it.temperature}.toString() + "°C"
                    findViewById<TextView>(R.id.HumValue).text = response.body()?.let {it.humidity}.toString() + "%"

                }
            })
        }




    }
}
data class HumTemp(val date_time : String, val humidity : Float, val temperature : Float)

interface HumTempService {
    @GET("/hum-temp/")
    fun getHumTemp(): Call<HumTemp>
}

data class CO2(val date_time : String, val co_value : Float, val co_warning : Int)

interface CO2Service {
    @GET("/co2/")
    fun getCO2(): Call<CO2>
}

