# ``WKInternalsNotes/_WKObservablePageState/_webProcessIsResponsive``

メインフレームの WebProcess が応答しているかを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) BOOL _webProcessIsResponsive;
```

## Default Value
既定値は `true`。

## Discussion
getter は `WebPageProxy` の `legacyMainFrameProcess` に対する `isResponsive()` を返す。応答性は `ResponsivenessTimer` と `BackgroundProcessResponsivenessTimer` の状態で決まる。

## References
- [`WKPagePrivateMac.mm#L101`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/C/mac/WKPagePrivateMac.mm#L101)
- [`WebProcessProxy.cpp#L1540`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/WebProcessProxy.cpp#L1540)
- [`ResponsivenessTimer.h#L92`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ResponsivenessTimer.h#L92)
- [`BackgroundProcessResponsivenessTimer.h#L67`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/BackgroundProcessResponsivenessTimer.h#L67)
- [`WKPagePrivateMac.h#L48`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/C/mac/WKPagePrivateMac.h#L48)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
