package com.example.myapplication;

public class Model {

    String date_time;
    Float co_value;
    Integer co_warning;


    public String getDate_time() {
        return date_time;
    }

    public void setDate_time(String date_time) {
        this.date_time = date_time;
    }

    public Float getCo_value() {
        return co_value;
    }

    public void setCo_value(Float co_value) {
        this.co_value = co_value;
    }

    public Integer getCo_warning() {
        return co_warning;
    }

    public void setCo_warning(Integer co_warning) {
        this.co_warning = co_warning;
    }
}
