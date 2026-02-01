# Write your MySQL query statement below
select s.student_id,s.student_name,subjects.subject_name,count(e.subject_name) as attended_exams from students as s
cross join subjects
left join examinations as e on s.student_id=e.student_id and
subjects.subject_name=e.subject_name
GROUP BY s.student_id, s.student_name, subjects.subject_name
order by s.student_id,subjects.subject_name asc;


