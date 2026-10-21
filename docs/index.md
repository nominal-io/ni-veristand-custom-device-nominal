% Ported from fern-docs 1dbaeb46 (fern/docs/pages/developers/documentation/connectors-and-sdks/veristand.mdx).

# NI VeriStand

Stream real-time test data from NI VeriStand® to Nominal. Nominal's custom device plugs into your VeriStand® system definition and publishes the channels you select while your real-time test runs.

Releases and source code are on [GitHub](https://github.com/nominal-io/ni-veristand-custom-device-nominal).

:::{note}
**New to VeriStand®?** NI VeriStand® is a configuration-based environment for real-time testing and hardware-in-the-loop (HIL) simulation. Custom devices extend VeriStand® with additional functionality. See [what is VeriStand](https://www.ni.com/en/shop/electronic-test-instrumentation/application-software-for-electronic-test-and-instrumentation-category/what-is-veristand.html).
:::

:::{warning}
The current release supports NI VeriStand® 2026 only.
:::

## Requirements

- NI VeriStand® 2026
- For NI® Linux® Real-Time targets, a way to deploy shared libraries to the target, such as shell access or NI SystemLink®

The custom device calls Nominal's libraries directly, so the [Nominal client for LabVIEW](site:/ni/labview/) is not required.

## Connect to Nominal

The custom device authenticates with a Nominal API key; see [API keys setup](site:/quickstart/quickstart/api-keys-setup/). It writes to either an asset RID paired with a dataset name, or a single [dataset RID](site:/quickstart/quickstart/quick/quick-dataset-rid/). See [Creating asset metadata](site:/quickstart/quickstart/quick/quick-asset/). Keep the API key secret; asset and dataset RIDs are identifiers rather than credentials.

## Install the custom device

1. Extract the release into `C:\Users\Public\Documents\National Instruments\NI VeriStand 2026\Custom Devices`.
2. Check that `Custom Device Nominal Core Streaming.xml` exists under `Custom Devices\Nominal Core Streaming\`. VeriStand® discovers the device the next time it launches.

## Deploy to real-time targets

Windows targets need nothing beyond the base VeriStand® installation.

NI® Linux® Real-Time targets need the device's shared libraries installed by hand. Copy both `.so` files from the device's `Linux_x64` folder to `/usr/local/lib` on the target, then run `ldconfig` as `admin`. The same work can be packaged for NI SystemLink®.

## Configure the custom device

### Add it to your system definition

In System Explorer, right-click **Custom Devices** under the target you want, then select **Nominal > Nominal Core Streaming**. The **CD Configuration** tab renames the instance and holds a description. A system definition can carry several instances, each with its own channels and settings.

### Enter your Nominal connection

On the **Nominal Configuration** tab, enter your API key in **Nominal API Key**, then choose a mode in **identifier selection**. **Asset Identifier and Dataset Name** writes to the dataset named in **Dataset Name** on the asset in **Asset RID**, matching an existing dataset by display name or refname and creating one if it finds none. **Dataset Identifier** writes straight to the dataset in **Dataset RID**. **Nominal Base URL** defaults to `https://api.gov.nominal.io/api/`. Change it if your instance uses a different URL. Set **Channel buffer size** to suit your control loop rate and latency budget.

### Pick channels to log

On the **Channel Configuration** tab, select **Add Channels**, choose the channels you want, and select **OK**.

### Map a time source

Map a time channel to the device's **Time source** channel, then set that channel's processing mode. The **to timestamp** mode converts the mapped value directly and pairs with the `Absolute Time` system channel, though the value is a double, so resolution suffers. The **relative seconds** mode treats the value as an offset from a start time the device sets when the engine begins execution, which gives better resolution at the cost of a possible fixed offset from absolute time. It pairs with the `System Time` system channel or an equivalent.

Nominal streams the selected channels in real time as your test executes.

### Choose which samples stream

The device's **Enable** and **Decimation** channels both default to 1, which streams every sample. Use **Enable** to stream only part of a test: at 0 the device drops samples but stays connected to Nominal, and any other value streams them again. Use **Decimation** to stream less often than your loop runs: at N the device streams every Nth sample, and 0 streams every sample.

## Trademarks

NI® (National Instruments®), NI VeriStand®, and NI SystemLink® are registered trademarks of NI®. Linux® is a registered trademark of Linus Torvalds. All other trademarks are the property of their respective owners.
