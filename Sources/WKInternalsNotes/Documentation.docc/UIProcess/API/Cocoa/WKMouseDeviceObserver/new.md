# ``WKInternalsNotes/WKMouseDeviceObserver/new()``

`new` は使用不可。

## Objective-C Declaration
```objective-c
+ (instancetype)new NS_UNAVAILABLE;
```

## Discussion
`sharedInstance` の利用を前提にしており、`new` は無効化されている。

## References
- [WKMouseDeviceObserver.h#L36](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKMouseDeviceObserver.h#L36)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
