import React from 'react';
import ReactDOM from 'react-dom';
import PropTypes from 'prop-types';
import styles from './MenuPage.module.scss';
import ScriptTag from 'react-script-tag';
import { Redirect } from 'react-router-dom';
import { connect } from 'react-redux';



const MenuPage = () => (
  <div className={styles.wrapper}>
    <h1>Menu</h1>


      {/* PLAY */}
      <div className={styles.card} style={{backgroundImage: `url('https://d21950x0o1sh55.cloudfront.net/assets/home/game-0e307d71d9838e8fbe4927b551f119bcd9e4748f2c2b70c7b81846702996ef94.jpg')`}}>
        <div className={styles.card__content}>
          <a className={styles.play_button}>
            <svg version="1.1" xmlns="http://www.w3.org/2000/svg" xmlnsXlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 50 50">
              <path d="M42.7,42.7L25,50L7.3,42.7L0,25L7.3,7.3L25,0l17.7,7.3L50,25L42.7,42.7z" className={styles.polygon}></path>
              <polygon points="32.5,25 21.5,31.4 21.5,18.6 "></polygon>
            </svg>
          </a>
          <div className={styles.card__content__description}>
            <h3 className={styles.roll_up}>
              <span><span>P</span><span>P</span></span>
              <span><span>l</span><span>l</span></span>
              <span><span>a</span><span>a</span></span>
              <span><span>y</span><span>y</span></span>
            </h3>
            <p className={styles.text_reveal}>
              <span>
                <span>And know more of</span>
                <span>the Everyday flaws</span>
                <span>that YOU make</span>
              </span>
              <span>
                <span><span>And know more of</span></span>
                <span><span>the Everyday flaws</span></span>
                <span><span>that YOU make</span></span>
              </span>
            </p>
          </div>
        </div>
      </div>


      {/* AVATAR */}
      <div className={styles.card} style={{backgroundImage: `url('https://d21950x0o1sh55.cloudfront.net/uploads/inside_exclusif/picture/26/desktop_VALERIAN_BNP_68.jpg')`}}>
        <div className={styles.card__content}>
          <a className={styles.play_button}>
            <svg version="1.1" xmlns="http://www.w3.org/2000/svg" xmlnsXlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 50 50">
              <path d="M42.7,42.7L25,50L7.3,42.7L0,25L7.3,7.3L25,0l17.7,7.3L50,25L42.7,42.7z" className={styles.polygon}></path>
              <polygon points="32.5,25 21.5,31.4 21.5,18.6 "></polygon>
            </svg>
          </a>
          <div className={styles.card__content__description}>
            <h3 className={styles.roll_up}>
              <span><span>A</span><span>A</span></span>
              <span><span>v</span><span>v</span></span>
              <span><span>a</span><span>a</span></span>
              <span><span>t</span><span>t</span></span>
              <span><span>a</span><span>a</span></span>
              <span><span>r</span><span>r</span></span>
            </h3>
            <p className={styles.text_reveal}>
              <span>
                <span>Customise</span>
                <span>Your profile</span>
              </span>
              <span>
                <span><span>Customise</span></span>
                <span><span>Your profile</span></span>
              </span>
            </p>
          </div>
        </div>
      </div>


      {/* CREW */}
      <div className={styles.card} style={{backgroundImage: `url('https://d21950x0o1sh55.cloudfront.net/uploads/inside_exclusif/picture/50/desktop_guided_tour_2.jpg')`}}>
        <div className={styles.card__content}>
          <a className={styles.play_button}>
            <svg version="1.1" xmlns="http://www.w3.org/2000/svg" xmlnsXlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 50 50">
              <path d="M42.7,42.7L25,50L7.3,42.7L0,25L7.3,7.3L25,0l17.7,7.3L50,25L42.7,42.7z" className={styles.polygon}></path>
              <polygon points="32.5,25 21.5,31.4 21.5,18.6 "></polygon>
            </svg>
          </a>
          <div className={styles.card__content__description}>
            <h3 className={styles.roll_up}>
              <span><span>C</span><span>C</span></span>
              <span><span>r</span><span>r</span></span>
              <span><span>e</span><span>e</span></span>
              <span><span>w</span><span>w</span></span>
            </h3>
            <p className={styles.text_reveal}>
              <span>
                <span>Who are we?</span>
                <span>Find out more about the makers</span>
              </span>
              <span>
                <span><span>Who are we?</span></span>
                <span><span>Find out more about the makers</span></span>
              </span>
            </p>
          </div>
        </div>
      </div>


      {/* SETTINGS */}
      <div className={styles.card} style={{backgroundImage: `url('https://d21950x0o1sh55.cloudfront.net/uploads/inside_exclusif/picture/6/desktop_VALERIAN_BNP_02.jpg')`}}>
        <div className={styles.card__content}>
          <a className={styles.play_button}>
            <svg version="1.1" xmlns="http://www.w3.org/2000/svg" xmlnsXlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 50 50">
              <path d="M42.7,42.7L25,50L7.3,42.7L0,25L7.3,7.3L25,0l17.7,7.3L50,25L42.7,42.7z" className={styles.polygon}></path>
              <polygon points="32.5,25 21.5,31.4 21.5,18.6 "></polygon>
            </svg>
          </a>
          <div className={styles.card__content__description}>
            <h3 className={styles.roll_up}>
              <span><span>S</span><span>S</span></span>
              <span><span>E</span><span>E</span></span>
              <span><span>T</span><span>T</span></span>
              <span><span>T</span><span>T</span></span>
              <span><span>I</span><span>I</span></span>
              <span><span>N</span><span>N</span></span>
              <span><span>G</span><span>G</span></span>
            </h3>
            <p className={styles.text_reveal}>
              <span>
                <span>Update Profile</span>
                <span>Manage Team</span>
              </span>
              <span>
                <span><span>Update Profile</span></span>
                <span><span>Manage Team</span></span>
              </span>
            </p>
          </div>
        </div>
      </div>
      <ScriptTag type='text/javascript' src='./Tilt.js'></ScriptTag>
      <ScriptTag type='text/javascript' src='https://cdnjs.cloudflare.com/ajax/libs/jquery/3.1.1/jquery.min.js'></ScriptTag>
  </div>
);

MenuPage.propTypes = {};

MenuPage.defaultProps = {};

export default MenuPage;
