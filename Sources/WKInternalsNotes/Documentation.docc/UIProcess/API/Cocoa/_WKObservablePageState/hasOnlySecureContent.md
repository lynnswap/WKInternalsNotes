# ``WKInternalsNotes/_WKObservablePageState/hasOnlySecureContent``

ページがセキュアコンテンツのみかを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) BOOL hasOnlySecureContent;
```

## Default Value
既定値は `false`。

## Discussion
getter は `PageLoadState::hasOnlySecureContent()` を返す。`hasInsecureContent` が `true` の場合は常に `false` になり、それ以外は `https` かどうかを `provisionalURL`（Provisional）または `url`（Committed/Finished）で判定する。

## References
- [`WKPagePrivateMac.mm#L96`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/C/mac/WKPagePrivateMac.mm#L96)
- [`PageLoadState.cpp#L218`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/PageLoadState.cpp#L218)
- [`PageLoadState.h#L224`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/PageLoadState.h#L224)
- [`WKPagePrivateMac.h#L47`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/C/mac/WKPagePrivateMac.h#L47)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
