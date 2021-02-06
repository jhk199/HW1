// Jack Kearney, 2/6/2021
package com.example.madlibs;

import android.content.Intent;
import android.graphics.Color;
import android.os.Bundle;
import android.os.Parcelable;
import android.util.Log;
import android.view.Gravity;
import android.view.View;
import android.widget.Button;
import android.widget.LinearLayout;
import android.widget.TextView;
import android.widget.Toast;

import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;

import com.google.android.material.textfield.TextInputEditText;

import org.json.JSONArray;
import org.json.JSONObject;

import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.List;

public class SecondActivity extends AppCompatActivity {

    private Button button_generate;
    private TextView title;
    private LinearLayout linearLayout;

    ArrayList<TextInputEditText> textInputList = new ArrayList<>(); // To keep track of TextInputs
    ArrayList<String> words = new ArrayList<>(); // From activity 1
    ArrayList<String> userWords = new ArrayList<>(); // User determined words
    ArrayList<String> text = new ArrayList<>(); // From activity 1

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_second);
        Intent oldIntent = getIntent();
        // importing the words and the text
        words = oldIntent.getStringArrayListExtra("words");
        text = oldIntent.getStringArrayListExtra("text");
        // Finding ids
        title = findViewById(R.id.textView_title_second);
        linearLayout = findViewById(R.id.second_linear_layout);
        button_generate = findViewById(R.id.button_generate);
        // Making the title
        title.setText(oldIntent.getStringExtra("title"));
        // Create the TextInputs with the Hints coming from the words
        printBlanks();
        // Log.d("editTexts", "" + textInputList.size());
    }

    public void launchNextActivity(View view) {
        sendWords(); // Put this into a separate function
    }

    public void sendWords() {
        for(TextInputEditText textInput : textInputList) { // Grabbing inputs to compare down below
            String text = textInput.getText().toString().trim();
            if(!text.equals("")) {
                userWords.add(text);
            }
        }
        if(userWords.size() == textInputList.size()) { // If you have enough filled out inputs
            // Log.d("", "Yes");
            Intent intent = new Intent(this, ThirdActivity.class);
            intent.putStringArrayListExtra("userWords", userWords);
            intent.putStringArrayListExtra("text", text);
            startActivity(intent);
        }
        else { // If you don't have all the text filled out, show a toast, yum
            Toast toast = Toast.makeText(this, R.string.toast_message, Toast.LENGTH_LONG);
            toast.setGravity(Gravity.TOP,0,250);
            toast.show();
            userWords.clear();
            // Log.d("", "No");
        }
    }

    public void printBlanks() {
        for (int i = 0; i < words.size(); i++) {
            TextInputEditText text_input = new TextInputEditText(this);
            textInputList.add(text_input);
            text_input.setHint(words.get(i)); // Setting hints from the words ArrayList
            linearLayout.addView(text_input);
        }
    }
}
// Jack Kearney, 2/6/2021
