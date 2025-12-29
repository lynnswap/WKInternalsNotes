# ``WKInternalsNotes/_WKObservablePageState/URL``

現在のアクティブ URL を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, copy) NSURL *URL;
```

## Default Value
初期値は `nil`（`activeURL` が空）。

## Discussion
getter は `PageLoadState::activeURL()` を `NSURL` に変換して返す。`activeURL` は `pendingAPIRequest` → `unreachableURL` → `provisionalURL`（Provisional）→ `url`（Committed/Finished）の順で選択される。

## References
- [`WKPagePrivateMac.mm#L91`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/C/mac/WKPagePrivateMac.mm#L91)
- [`PageLoadState.cpp#L195`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/PageLoadState.cpp#L195)
- [`PageLoadState.h#L230`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/PageLoadState.h#L230)
- [`WKPagePrivateMac.h#L44`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/C/mac/WKPagePrivateMac.h#L44)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
