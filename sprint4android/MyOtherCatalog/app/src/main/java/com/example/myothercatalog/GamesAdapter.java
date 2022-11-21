package com.example.myothercatalog;


import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

public class GamesAdapter extends RecyclerView.Adapter<GamesViewHolder> {
    private GamesList games;

    public GamesAdapter(GamesList games) {
        this.games=games;
    }

    @NonNull
    @Override
    public GamesViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        LayoutInflater inflater = LayoutInflater.from(parent.getContext());
        View view = inflater.inflate(R.layout.game_recycler_cell, parent, false);
        GamesViewHolder viewHolder = new GamesViewHolder(view);
        return viewHolder;
    }

    @Override
    public void onBindViewHolder(@NonNull GamesViewHolder holder, int position) {
        Game data = this.games.getGames().get(position);
        holder.ShowData(data);
    }

    @Override
    public int getItemCount() {
        int items = this.games.getGames().size();
        return items;
    }
}

