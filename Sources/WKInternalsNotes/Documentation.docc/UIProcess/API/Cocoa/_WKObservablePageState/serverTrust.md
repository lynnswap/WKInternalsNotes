# ``WKInternalsNotes/_WKObservablePageState/serverTrust``

現在のページのサーバ証明書（`SecTrustRef`）を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) SecTrustRef serverTrust;
```

## Default Value
初期値は `nil`。

## Discussion
KVO 非対応。getter は `pageLoadState().certificateInfo().trust().get()` を返す。

## References
- [`WKPagePrivateMac.mm#L116`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/C/mac/WKPagePrivateMac.mm#L116)
- [`PageLoadState.h#L248`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/PageLoadState.h#L248)
- [`WKPagePrivateMac.h#L52`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/C/mac/WKPagePrivateMac.h#L52)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
