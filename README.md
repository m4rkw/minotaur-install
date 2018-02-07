# Minotaur installer

## Overview

From a minimal Centos 7 install, this will install:

- Minotaur
- Fanotaur
- Excavataur

and miners: excavator, ccminer, ccminer2 and ethminer.

All will run on startup. You should adjust the configuration to your needs.

## Usage

````
curl https://rkw.io/minotaur | bash
````

Then reboot the system.

This will deploy:

- xorg with appropriate config for all Nvidia devices on the system
- a "miner" user to run the applications with
- fanotaur - starting on boot
- excavator - starting on boot
- excavataur - starting on boot
- ccminer
- ccminer2
- ethminer
- gs display for minotaur - starting on boot

minotaur itself will not start on boot but you can change this by uncommenting
the line for it in /etc/rc.local. First you will probably want to do some
calibration though - see the README in the minotaur project for details.

All of the startup applications will run in screen sessions owned by the miner
user. You should run minotaur as the miner user, eg:

````
sudo su miner
````

then you can see the list of screen sessions with:

````
screen -list
````

jump into one with -r, eg to see the gs display:

````
screen -r gs
````

to exit from a screen session press ctrl-a and then d.

## Disclaimer

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
