package com.example.myothercatalog;

import android.view.View;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

public class GamesViewHolder extends RecyclerView.ViewHolder {
    private ImageView image;
    private TextView name;
    private TextView description;

    public GamesViewHolder(@NonNull View itemView) {
        super(itemView);
        image = itemView.findViewById(R.id.game);
        name = itemView.findViewById(R.id.title);
        description = itemView.findViewById(R.id.description);
    }

    public void ShowData(Game game){
        Util.downloadBitmapToImageView(game.getImageUrl(), this.image);
        this.name.setText(game.getName());
        this.description.setText(game.getDescription());
    }
}
