import sys,os
from string import strip,split,find

route_dict = {
    '1': '1143',
    '2': '1144',
    '3': '1145',   
    '4': '1146',    
    '5': '1147',    
    '7': '1148',    
    '9': '1149',    
    '10': '1150',    
    '11': '1151',    
    '111': '1152',    
    '12': '1153',    
    '13': '1154',    
    '14': '1155',    
    '16': '1156',    
    '17': '1157',    
    '1717': '1158',    
    '18': '1159',    
    '19': '1160',    
    '20': '1161',    
    '2020': '1162',    
    '21': '1163',    
    '23': '1164',    
    '2323': '1165',    
    '25': '1166',    
    '26': '1167',    
    '26 SAT': '1168',    
    '29': '1169',    
    '29 SAT': '1170',    
    '2929': '1171',    
    '30': '1172',    
    '40': '1173',   
    '43': '1174',    
    '44': '1175',    
    '444': '1176',    
    '1D': '1177',    
    '71': '1293',    
    '710': '1294',    
    '713': '1295',    
    '717': '1296',    
    '720': '1297',    
    '729': '1298',    
    '74': '1299',    
}


def fixFields(line):
    (route_id,agency_id,route_short_name,route_long_name,route_desc,route_type,route_url,route_color,route_text_color) = line.split(",")
    route_short_name = route_short_name.strip()

    if route_short_name in route_dict:
        route_id = route_dict[route_short_name]
    else:
        print "WARNING: Route \'%s\' not found in dict" % route_short_name
    
    return ','.join([route_id,agency_id,route_short_name,route_long_name,route_desc,route_type,route_url,route_color,route_text_color])


    
def main():

    try :
        inFileName,outFileName = sys.argv[1:]
        print inFileName
    except ValueError:
        print "Usage: editGtfsRouteId.py <inFileName> <outFileName>"
        sys.exit(2)

    
    inLines = open(inFileName,'r').readlines()
    outLines = open(outFileName,'w')

    print "Now going to read " + inFileName
    for line in inLines:
        fixLine = fixFields(line)
        outLines.write(fixLine)

    print "Changes complete!"
        
        
    outLines.close()

if __name__ == "__main__":
    main()
