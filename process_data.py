import datetime

def process_data(filename):
    teams = ["AST", "XL", "S04", "FNC", "G2", "MAD", "MSF", "RGE", "SK", "VIT"]
    
    file_obj = open(filename, "r")
    lines = file_obj.readlines()[1:]
    
    sez_igr = []
    
    for i in range(len(lines)):
        line = lines[i].split(";")
        current_team = teams[i]

        for j in range(len(line)):
            game = line[j]
            current_opponent = teams[j]

            if game == "/":
                continue
            else:
                ref_team, ref_opp, date = game.split(",")
                
                ref_team = ref_team.replace("(", "")
                
                date = date.replace(")", "").split(".")
                date = datetime.datetime(2021, int(date[1]), int(date[0]))

                if ref_team == "1":
                    ref_tuple = (current_team, current_opponent, current_team, date)
                else:
                    ref_tuple = (current_team, current_opponent, current_opponent, date)
                
                sez_igr.append(ref_tuple)

    sortirano = sorted(sez_igr, key= lambda x: x[3])
    packed = [(t1, t2, win) for t1, t2, win, _ in sortirano]
    return packed[:int(len(packed)/2)], packed[int(len(packed)/2):]
        

if __name__ == "__main__":
    train, test = process_data("data.txt")
    print(train)
    print(test)
