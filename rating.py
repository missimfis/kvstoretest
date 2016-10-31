import ch.icclab.cyclops.facts.model.rcb.chargedata.ChargeData;
import ch.icclab.cyclops.facts.model.rcb.usagedata.Storage;
rule "Rate Storage usage data"
when
$usage: Storage()
then
ChargeData charge = new ChargeData($usage);
charge.setCharge($usage.getUsage() * 10);
insert(charge);
retract($usage);
end
