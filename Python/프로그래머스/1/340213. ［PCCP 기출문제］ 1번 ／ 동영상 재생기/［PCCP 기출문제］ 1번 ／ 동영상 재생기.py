def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    pos_sec = int(pos[0])*600 + int(pos[1])*60+int(pos[3])*10+int(pos[4])
    op_start_sec = int(op_start[0])*600 + int(op_start[1])*60+int(op_start[3])*10+int(op_start[4])
    op_end_sec = int(op_end[0])*600 + int(op_end[1])*60+int(op_end[3])*10+int(op_end[4])
    video_len_sec = int(video_len[0])*600 + int(video_len[1])*60+int(video_len[3])*10+int(video_len[4])
    if pos_sec >= op_start_sec and pos_sec <= op_end_sec:
            pos_sec = op_end_sec
    for i in commands:
        if i =="prev":
            pos_sec -= 10
            
            if pos_sec <10:
                pos_sec = 0
        elif i =="next":
            pos_sec += 10
            
            if video_len_sec-pos_sec <10:
                pos_sec = video_len_sec
            
        if pos_sec >= op_start_sec and pos_sec <= op_end_sec:
            pos_sec = op_end_sec
    answer+=str(pos_sec//600)
    pos_sec = pos_sec % 600
    answer+=str(pos_sec//60)
    pos_sec = pos_sec % 60
    answer+=":"
    answer+=str(pos_sec//10)
    pos_sec = pos_sec % 10
    answer+=str(pos_sec)
    return answer

