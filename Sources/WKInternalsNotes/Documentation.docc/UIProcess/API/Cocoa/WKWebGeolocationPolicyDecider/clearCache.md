# ``WKInternalsNotes/WKWebGeolocationPolicyDecider/clearCache()``

Geolocation の許可履歴キャッシュをクリアする。

## Objective-C Declaration
```objective-c
- (void)clearCache;
```

## Discussion
メモリ上の `_sites` を破棄し、ディスク上の `GeolocationSitesV2.plist` を非同期で削除する。次回の `_loadWithCompletionHandler` でファイルを再読み込みし直すため、チャレンジ履歴がリセットされる。

## References
- [`WKWebGeolocationPolicyDecider.h#L43`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKWebGeolocationPolicyDecider.h#L43)
- [`WKWebGeolocationPolicyDeciderIOS.mm#L219`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKWebGeolocationPolicyDeciderIOS.mm#L219)
- [`WKWebGeolocationPolicyDeciderIOS.mm#L223`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKWebGeolocationPolicyDeciderIOS.mm#L223)
- [`WKWebGeolocationPolicyDeciderIOS.mm#L228`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKWebGeolocationPolicyDeciderIOS.mm#L228)
- [`WKWebGeolocationPolicyDeciderIOS.mm#L233`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKWebGeolocationPolicyDeciderIOS.mm#L233)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
