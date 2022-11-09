class colorPallete:
    def __init__(
        self,
        max_colors = 8,
        ignore_colors = {"misc"},
        pallete={
        "orange": {
                "orange": "F1641E",
                "orange_dark": "CF4018",
                "orange_light": "FAA077",
                "orange_tint": "F8EBE6",
                "orange_tint_dm": "D8C4BC",
        },
        "denim": {
                "denim": "2F466C",
                "denim_dark": "232347",
                "denim_dm": "426194",
                "denim_light": "4D6BC6",
                "denim_light_dm": "829CEE",
                "denim_tint": "D7E6F5",
                "denim_tint_dm": "B5C6D8",
        },
        "lavender": {
                "lavender": "654B77",
                "lavender_dark": "3E1C53",
                "lavender_dark_dm": "4F2469",
                "lavender_light": "9560B8",
                "lavender_tint": "E6E1F0",
                "lavender_tint_dm": "CAC1DB"
        },
        "beeswax": {
                "beeswax": "FAA129",
                "beeswax_dark": "A66800",
                "beeswax_dark_dm": "DB8B00",
                "beeswax_light": "FDD95C",
                "beeswax_tint": "FDEBD2",
                "beeswax_tint_dm": "E2D3BD",
        },
        "slime" : {
                "slime": "258635",
                "slime_dark": "1C4A21",
                "slime_dark_dm": "215E28",
                "slime_dm": "54B063",
                "slime_light": "9EC063",
                "slime_tint": "D4E9D7",
                "slime_tint_dm": "96B09B"
        },
        "turquoise": {
                    "turquoise": "2F766D",
                    "turquoise_dark": "1A3B38",
                    "turquoise_dark_dm": "20524D",
                    "turquoise_light": "7ED4BD",
                    "turquoise_tint": "DDEBE3",
                    "turquoise_tint_dm": "C6D7CD"
        },
        "bubblegum": {

                "bubblegum": "B54C82",
                "bubblegum_dark": "592642",
                "bubblegum_light": "F592B8",
                "bubblegum_tint": "F5D9E3",
        },     
        "brick": {
                "brick": "A61A3E",
                "brick_dark": "540D17",
                "brick_dark_dm": "731F2B",
                "brick_light": "FD9184",
                "brick_light_dm": "F27878",
                "brick_tint": "FDDCD8",
                "brick_tint_dm": "CA9E99",
            },
        "misc": {
                "aluminum": "9E9E9E",
                "black": "222222",
                "charcoal": "595959",
                "ice": "EAEAEA",
                "silver": "D3D3D3",
                "snow": "F2F2F2",
                "steel": "757575",
                "stone": "DEDEDE",
                "white": "FFFFFF",
        },
    }

    ):
        self.pallete = pallete
        self.colors_dict = self.generate_n_colors(max_colors, ignore_colors)
        
    def gimme_colors(self, n_colors):
        colors_generated = 0
        results = []
        for color_name, color_hex in self.colors_dict.items():
            if colors_generated < n_colors:
                colors_generated = colors_generated + 1
                color_hex = "#" + color_hex
                results.append(color_hex)
        return results
            
        
    def print_default_colors(self):
        for key in self.pallete.keys():
            if key == "misc":
                continue
            hex = self.pallete[key][key]
            hex = "#" + hex
            print(key, hex)
            
    def generate_n_colors(self, max_colors=8, ignore_colors={"misc"},):
        all_colors = {}
        pallets = ["_light"]
        if max_colors > 8:
            pallets.append("default")
        if max_colors>16:
            pallets.append("_dark")
        if max_colors >= 22:
            print("You need to use fewer colors friend")
            assert 1==2
        
        for pallet in pallets:
            for color_name, color_pallete in self.pallete.items():
                if color_name not in ignore_colors:
                    if pallet != "default":
                        color_name = color_name + pallet
                    all_colors[color_name] = color_pallete[color_name]
        
        # -- If you ignored a default color and need more we will pad with misc etsy colors
        if len(all_colors) < max_colors:
            for color_name, color_hex in self.pallete["misc"].items():
                print(color_hex)
                all_colors[color_name] = color_hex

        
        return all_colors
                
etsy_colors = colorPallete(max_colors=21)
pallete_2 = etsy_colors.gimme_colors(n_colors=2)
pallete_8 = etsy_colors.gimme_colors(n_colors=8)
pallete_20 = etsy_colors.gimme_colors(n_colors=20)