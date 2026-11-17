import json
CSS='''.svf{max-width:920px;margin:0 auto;background:#fff;border:1px solid var(--line);border-radius:var(--r);padding:36px;box-shadow:0 20px 50px rgba(11,42,28,.08)}
.svf fieldset{border:0;margin:0 0 22px;padding:0;min-width:0}.svf legend{font-weight:700;color:var(--g2);margin-bottom:12px;font-size:1rem}
.cal{display:grid;grid-template-columns:repeat(7,1fr);gap:6px}.cal .wh{font-size:.72rem;font-weight:700;text-transform:uppercase;letter-spacing:.08em;color:var(--mut);text-align:center;padding-bottom:4px}
.cal button,.slots button{font:inherit;border:1px solid #cfd3cf;background:#fff;color:var(--ink);border-radius:var(--r);cursor:pointer;min-height:48px}
.cal button{min-height:66px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:1px;padding:4px 2px}.cal button b{font-size:1.1rem;line-height:1.1}.cal button small{font-size:.68rem;color:var(--mut)}
.cal button.we{background:#f6efe2;border-color:var(--au)}.cal button.we small{color:var(--aud)}
.cal button:disabled{background:#f1f1ef;color:#6b6f6c;cursor:not-allowed;border-style:dashed}.cal button:disabled small{color:#6b6f6c}
.cal button:not(:disabled):hover,.slots button:not(:disabled):hover{border-color:var(--g)}
.cal button[aria-pressed=true],.slots button[aria-pressed=true]{background:var(--g);border-color:var(--g);color:#fff}.cal button[aria-pressed=true] small{color:#e8efe9}
.slots{display:grid;grid-template-columns:repeat(auto-fill,minmax(112px,1fr));gap:8px}.slots button{padding:0 10px;font-weight:600}.slots button:disabled{color:#6b6f6c;background:#f1f1ef;cursor:not-allowed;text-decoration:line-through}
.svlg{display:flex;gap:18px;flex-wrap:wrap;font-size:.8rem;color:var(--mut);margin-top:10px}.svlg i{display:inline-block;width:14px;height:14px;border:1px solid var(--au);background:#f6efe2;vertical-align:-2px;margin-right:6px;border-radius:2px}.svlg i.c{background:#f1f1ef;border:1px dashed #6b6f6c}
.svr{display:grid;grid-template-columns:1fr 1fr;gap:16px}.svf .note{font-size:.85rem;color:var(--mut);margin-top:10px}.er2{color:#a32b2b;margin-top:10px}
@media(max-width:760px){.svf{padding:22px 16px}.cal{display:flex;overflow-x:auto;gap:8px;padding-bottom:6px;scroll-snap-type:x proximity}.cal .wh,.cal .bl{display:none}.cal button{flex:0 0 64px;scroll-snap-align:start}.svr{grid-template-columns:1fr}}'''
def section(T,lang):
  return f'''<section class="sec" id="visit"><div class="wrap"><div class="hd c rv"><span class="kick">{T['kick']}</span><h2>{T['h']}</h2><p>{T['p']}</p></div>
<form id="sv" class="svf" novalidate aria-labelledby="svh"><h3 id="svh" class="vh">{T['h']}</h3>
<fieldset><legend>{T['l1']}</legend><div class="cal" id="svd" role="group" aria-label="{T['l1']}" aria-describedby="sve-d"></div><p class="svlg"><span><i></i>{T['wk']}</span><span><i class="c"></i>{T['cl']}</span></p><small class="err" id="sve-d" role="alert"></small></fieldset>
<fieldset><legend>{T['l2']}</legend><div class="slots" id="svs" role="group" aria-label="{T['l2']}" aria-describedby="sve-s"></div><small class="err" id="sve-s" role="alert"></small></fieldset>
<fieldset><legend>{T['l3']}</legend><div class="svr"><div class="fld"><label for="sv-name">{T['name']}</label><input id="sv-name" name="name" autocomplete="name" aria-describedby="sve-name" placeholder="{T['ph1']}" required maxlength="100"><small class="err" id="sve-name"></small></div><div class="fld"><label for="sv-phone">{T['phone']}</label><input id="sv-phone" name="phone" type="tel" autocomplete="tel" inputmode="tel" pattern="[0-9+ ()-]{{10,20}}" aria-describedby="sve-phone" placeholder="{T['ph2']}" required maxlength="20"><small class="err" id="sve-phone"></small></div></div><input name="website" class="hp" tabindex="-1" autocomplete="off" aria-hidden="true"></fieldset>
<button class="btn" type="submit">{T['submit']}</button><p class="note">{T['note']}</p><div id="svmsg" role="status" aria-live="polite"></div></form>
<script type="application/json" id="svt">{json.dumps({k:T[k] for k in ['closed','closedS','weekend','eName','ePhone','ePhone2','eDate','eSlot','sending','fail','submit']},ensure_ascii=False)}</script></div></section>
'''
CSS+='#sv button[type=submit]{align-self:end;height:auto;min-height:48px}'
