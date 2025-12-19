# ``WKInternalsNotes/WKScreenTimeConfigurationObserver/startObserving()``

Screen Time 設定の監視を開始する。

## Objective-C Declaration
```objective-c
- (void)startObserving;
```

## Discussion
`STScreenTimeConfigurationObserver` を生成し、`configuration.enforcesChildRestrictions` の KVO を設定して監視を開始する。

## References
- [`WKScreenTimeConfigurationObserver.h#L34`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/WKScreenTimeConfigurationObserver.h#L34)
- [`WKScreenTimeConfigurationObserver.mm#L67`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/WKScreenTimeConfigurationObserver.mm#L67)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
