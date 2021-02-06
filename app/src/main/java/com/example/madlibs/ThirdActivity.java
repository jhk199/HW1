// Jack Kearney, 2/6/2021
package com.example.madlibs;

import android.content.Intent;
import android.graphics.Color;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.LinearLayout;
import android.widget.TextView;

import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;

import java.util.ArrayList;

public class ThirdActivity extends AppCompatActivity {

    private Button button_home;
    ArrayList<String> userWords = new ArrayList<>();
    ArrayList<String> text = new ArrayList<>();
    String result= "";
    private LinearLayout linearLayout;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_third);
        Intent oldIntent = getIntent();

        userWords = oldIntent.getStringArrayListExtra("userWords");
        text = oldIntent.getStringArrayListExtra("text");

        // Log.d("User words", userWords.toString());
        // Log.d("text", text.toString());

        linearLayout = findViewById(R.id.third_linear_layout);
        button_home = findViewById(R.id.button_home);
        generateMadLib();
    }

    // Go back to home
    public void launchNextActivity(View view) {
        Intent intent = new Intent(this, MainActivity.class);
        startActivity(intent);
    }

    public void generateMadLib() {
        TextView textView = new TextView(this);
        mergeArrays(text, userWords);
        textView.setText(result);
        textView.setTextSize(30);
        textView.setTextColor(Color.BLACK);
        linearLayout.addView(textView);
        Log.d("result", result);
    }

    // This function combines the two ArrayLists into a single string to display in a TextView
    public void mergeArrays(ArrayList one, ArrayList two) {
        int i = 0, j = 0;
        one.remove(one.size() - 1);
        while(i < one.size() || j < two.size()) {
            if(i < one.size()) {
                result +=  ((String) one.get(i++));
            }
            if(j < two.size()) {
                result += ((String) two.get(j++));
            }
        }
    }
}
// Jack Kearney, 2/6/2021
