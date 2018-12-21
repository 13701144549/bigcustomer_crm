namespace py spring

service Spring {
    void ping();
    i64 getid();
    list<i64> getids(1:i32 num);
    string getsn(1:i32 biz_id);
    string getssn(); //short
}

