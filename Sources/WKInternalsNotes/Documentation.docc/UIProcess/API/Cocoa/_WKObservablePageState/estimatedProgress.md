# ``WKInternalsNotes/_WKObservablePageState/estimatedProgress``

ページ読み込み進捗の推定値を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) double estimatedProgress;
```

## Default Value
既定値は `0`。

## Discussion
getter は `WebPageProxy::estimatedProgress()` を返し、内部的には `PageLoadState::estimatedProgress()` に委譲する。`pendingAPIRequest` がある場合は `initialProgressValue`（0.1）を返す。

## References
- [`WKPagePrivateMac.mm#L106`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/C/mac/WKPagePrivateMac.mm#L106)
- [`WebPageProxy.cpp#L6668`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/WebPageProxy.cpp#L6668)
- [`PageLoadState.cpp#L245`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/PageLoadState.cpp#L245)
- [`PageLoadState.h#L245`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/PageLoadState.h#L245)
- [`WKPagePrivateMac.h#L46`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/C/mac/WKPagePrivateMac.h#L46)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
