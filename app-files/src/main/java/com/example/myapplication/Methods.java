package com.example.myapplication;

import retrofit2.Call;
import retrofit2.http.GET;

public interface Methods {

    @GET("co2/")
    Call<Model> getAllData();
}
