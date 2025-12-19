# ``WKInternalsNotes/WKWebView/_didFinishLoadingDataForCustomContentProviderWithSuggestedFilename(_:data:)``

`_didFinishLoadingDataForCustomContentProviderWithSuggestedFilename` を実行する。

## Objective-C Declaration
```objective-c
- (void)_didFinishLoadingDataForCustomContentProviderWithSuggestedFilename:(const WTF::String&)suggestedFilename data:(NSData *)data;
```

## Discussion
実装は `WKWebView` 側で処理される。

## References
- [`WKWebViewIOS.h#L94`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/ios/WKWebViewIOS.h#L94)
- [`WKWebViewIOS.mm#L605`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/ios/WKWebViewIOS.mm#L605)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
