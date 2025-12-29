# ``WKInternalsNotes/_WKObservablePageState/unreachableURL``

到達不能だった URL を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) NSURL *unreachableURL;
```

## Default Value
初期値は `nil`（`unreachableURL` 未設定時）。

## Discussion
KVO 非対応。getter は `pageLoadState().unreachableURL()` を `NSURL` に変換して返す。

## References
- [`WKPagePrivateMac.mm#L111`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/C/mac/WKPagePrivateMac.mm#L111)
- [`PageLoadState.h#L234`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/PageLoadState.h#L234)
- [`WKPagePrivateMac.h#L51`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/C/mac/WKPagePrivateMac.h#L51)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
