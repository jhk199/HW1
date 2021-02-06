// Jack Kearney, 2/6/2021
package com.example.madlibs;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;

import com.loopj.android.http.AsyncHttpClient;
import com.loopj.android.http.AsyncHttpResponseHandler;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.util.ArrayList;

import cz.msebera.android.httpclient.Header;

public class MainActivity extends AppCompatActivity {

    private Button button_go;

    // API call stuff

    ArrayList<String> words = new ArrayList<>(); // stores words from api
    ArrayList<String> text = new ArrayList<>(); // stores text from api
    private static final String api_url = "http://madlibz.herokuapp.com/api/random?minlength=5&maxlength=10";
    private static AsyncHttpClient client = new AsyncHttpClient();
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        button_go = findViewById(R.id.button_go);
    }

    public void launchNextActivity(View view) {
        client.get(api_url, new AsyncHttpResponseHandler() {
            @Override
            public void onSuccess(int statusCode, Header[] headers, byte[] responseBody) {
                // Log.d("api response",new String(responseBody));
                try {
                    Intent intent = new Intent(MainActivity.this, SecondActivity.class);
                    JSONObject json = new JSONObject(new String(responseBody));
                    String title = json.getString("title");
                    JSONArray blanks = json.getJSONArray("blanks");
                    JSONArray value = json.getJSONArray("value");
                    for(int i = 0; i < blanks.length(); i++) { // JSONArray to ArrayList for words
                        words.add(blanks.getString(i));
                    }
                    for(int i = 0; i < value.length(); i++) { // JSONArray to ArrayList for text
                        text.add(value.getString(i));
                    }
                    intent.putExtra("title", title);
                    intent.putStringArrayListExtra("words", words); // passing array of words
                    intent.putStringArrayListExtra("text", text); // passing array of words
                    startActivity(intent);
                } catch (JSONException e) {
                    e.printStackTrace();
                }
            }

            @Override
            public void onFailure(int statusCode, Header[] headers, byte[] responseBody, Throwable error) {

            }
        });

    }
}
// Jack Kearney, 2/6/2021