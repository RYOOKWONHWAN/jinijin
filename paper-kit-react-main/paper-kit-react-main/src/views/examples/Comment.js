import React, { useState } from 'react';
import { Button, Modal } from "react-bootstrap";


const Comments = () => {
  const [show, setShow] = useState(false);
  
  const handleClose = () => setShow(false);
  const handleShow = () => setShow(true);
  return (

    <div className="container d-flex justify-content-center align-items-center" style={{ backgroundColor: 'white', marginTop: '250px' }}>
      <div className="container">
        <header className="my-4">
          <div className="row">
            <div className="col-12">
              <h2 className="text-center">1</h2>
              <p className="text-center">작품을 평가해보세요. 당신의 취향에 딱 맞는 작품을 추천해드릴게요.</p>
            </div>
          </div>
        </header>
        <div className="row">
          <div className="col-12">
            <ul className="list-unstyled d-flex justify-content-around">
              <li>영화</li>
              <li>TV 프로그램</li>
              <li>책</li>
              <li>웹툰</li>
            </ul>
          </div>
        </div>
        <div className="d-flex justify-content-between mt-4">
          <div className="arrow_button css-38kpup" direction="left"><div className="css-1hestod"></div></div>
          <div className="arrow_button css-h5qs9h" direction="right"><div className="css-vp7uyl"><img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMiIgaGVpZ2h0PSIxNiIgdmlld0JveD0iMCAwIDEyIDE2Ij4KICAgIDxnIGZpbGw9Im5vbmUiIGZpbGwtcnVsZT0iZXZlbm9kZCI+CiAgICAgICAgPHBhdGggZD0iTTAgMEgxNkgweiIvPgogICAgICAgIDxwYXRoIGZpbGw9IiMyOTJBMzIiIHN0cm9rZT0iIzI5MkEzMiIgc3Ryb2tlLXdpZHRoPSIuMzUiIGQ9Ik0zLjQyOSAxMy40MDlMNC4zNTQgMTQuMjU4IDEwLjY4IDguNDYgMTEuMTQzIDguMDM2IDQuMzU0IDEuODEzIDMuNDI5IDIuNjYyIDkuMjkxIDguMDM2eiIvPgogICAgPC9nPgo8L3N2Zz4K" alt="forward" /></div>
          </div>
        </div>
        <div className="d-flex justify-content-start mt-4">
          <button className="btn btn-primary">랜덤 영화</button>
        </div>
        <div className="row">
          <div className="col">

            <ul>
              <li className="list-group-item">
                <div className="row align-items-center">
                  <div className="col-3">

                    <img src="https://an2-img.amz.wtchn.net/image/v2/cieT7gGSMHncWBrbSgOqeg.jpg?jwt=ZXlKaGJHY2lPaUpJVXpJMU5pSjkuZXlKdmNIUnpJanBiSW1SZk1qZ3dlRFF3TUhFNE1DSmRMQ0p3SWpvaUwzWXhMMmhxY1hkaWNHaHdaRzV6ZERSa2JXZGpkVFY2SW4wLmxmQ0dlNFNFcG1VYWtGTVM1b3htOFJqaTVFZ2hXX2VrVnVVZHZ6VDExMUE" alt="movie" className="img-fluid" />
                  </div>
                  <div className="col-9">
                    <h3 className="mb-0">살인자의 기억법</h3>
                    <div>2016 ・ 한국</div>
                  </div>
                </div>
              </li>
              <li className="list-group-item">
                <div className="row align-items-center">
                  <div className="col-3">
                    <img src="https://an2-img.amz.wtchn.net/image/v2/cieT7gGSMHncWBrbSgOqeg.jpg?jwt=ZXlKaGJHY2lPaUpJVXpJMU5pSjkuZXlKdmNIUnpJanBiSW1SZk1qZ3dlRFF3TUhFNE1DSmRMQ0p3SWpvaUwzWXhMMmhxY1hkaWNHaHdaRzV6ZERSa2JXZGpkVFY2SW4wLmxmQ0dlNFNFcG1VYWtGTVM1b3htOFJqaTVFZ2hXX2VrVnVVZHZ6VDExMUE" alt="movie" className="img-fluid" />
                  </div>
                  <div className="col-9">
                    <h3 className="mb-0">살인자의 기억법</h3>
                    <div>2016 ・ 한국</div>
                  </div>
                </div>
              </li>
              <li className="list-group-item">
                <div className="row align-items-center">
                  <div className="col-3">
                    <img src="https://an2-img.amz.wtchn.net/image/v2/cieT7gGSMHncWBrbSgOqeg.jpg?jwt=ZXlKaGJHY2lPaUpJVXpJMU5pSjkuZXlKdmNIUnpJanBiSW1SZk1qZ3dlRFF3TUhFNE1DSmRMQ0p3SWpvaUwzWXhMMmhxY1hkaWNHaHdaRzV6ZERSa2JXZGpkVFY2SW4wLmxmQ0dlNFNFcG1VYWtGTVM1b3htOFJqaTVFZ2hXX2VrVnVVZHZ6VDExMUE" alt="movie" className="img-fluid" />
                  </div>
                  <div className="col-9">
                    <h3 className="mb-0">살인자의 기억법</h3>
                    <div>2016 ・ 한국</div>
                    <Button variant="primary" onClick={handleShow}>
                      자세히 보기
                    </Button>
                    <Modal show={show} onHide={handleClose}>
                      <Modal.Header closeButton>
                        <Modal.Title>영화 상세정보</Modal.Title>
                      </Modal.Header>
                      <Modal.Body>
                        <p>영화 제목: 살인자의 기억법</p>
                        <p>개봉 연도: 2016</p>
                        <p>국가: 한국</p>
                        <p>감독: 김태균</p>
                        <p>출연: 서인국, 나문희, 김성균</p>
                        <p>
                          줄거리: 살인사건의 유일한 증인이 된 여자가, 자신이 목격한 살인범의 얼굴을
                          잊어버리는 질병에 걸리자, 살인범을 찾아내기 위해 노력하는 사건을 그린 스릴러
                          영화입니다.
                        </p>
                      </Modal.Body>
                      <Modal.Footer>
                        <Button variant="secondary" onClick={handleClose}>
                          닫기
                        </Button>
                      </Modal.Footer>
                    </Modal>
                  </div>
                </div>
              </li>


            </ul>
          </div>

        </div>

      </div>

      <div className="row">
        <div className="col">

        </div>
      </div>


    </div>


  )
}

export default Comments
