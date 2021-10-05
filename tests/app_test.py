def test_get_assignments_student_1(client, h_student_1):
    response = client.get(
        '/',
    )

    assert response.status_code == 200