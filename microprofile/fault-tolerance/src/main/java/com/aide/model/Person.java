package com.aide.model;

public class Person {
    private Long personID;
    private String name;
    private String email;

    public Person() {

    }

    public Person(Long personID, String name, String email) {
        this.personID = personID;
        this.name = name;
        this.email = email;
    }

    public Long getPersonID() {
        return personID;
    }

    public void setPersonID(Long personID) {
        this.personID = personID;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
}
