package com.example.myothercatalog;


import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.util.ArrayList;
import java.util.List;

public class GamesList {
    private List<Game> games;

    public GamesList(JSONArray array){
        games = new ArrayList<>();
        for(int i=0;i<array.length();i++){
            try {
                JSONObject jsonElement = array.getJSONObject(i);
                Game game = new Game(jsonElement);
                games.add(game);
            }
            catch (JSONException ex){
                throw new RuntimeException(ex);
            }
        }
    }

    public List<Game> getGames() {
        return games;
    }
}
