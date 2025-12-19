# ``WKInternalsNotes/WKScreenTimeConfigurationObserver/stopObserving()``

Screen Time 設定の監視を停止する。

## Objective-C Declaration
```objective-c
- (void)stopObserving;
```

## Discussion
監視を停止し、KVO を解除してオブザーバを破棄する。

## References
- [`WKScreenTimeConfigurationObserver.h#L35`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/WKScreenTimeConfigurationObserver.h#L35)
- [`WKScreenTimeConfigurationObserver.mm#L77`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/WKScreenTimeConfigurationObserver.mm#L77)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
