# ``WKInternalsNotes/_WKObservablePageState/loading``

ページが読み込み中かを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, getter=isLoading) BOOL loading;
```

## Default Value
既定値は `false`。

## Discussion
getter は `PageLoadState::isLoading()` を返す。`pendingAPIRequest` がある場合、または状態が Provisional/Committed の場合に `true` になる。

## References
- [`WKPagePrivateMac.mm#L81`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/C/mac/WKPagePrivateMac.mm#L81)
- [`PageLoadState.cpp#L441`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/PageLoadState.cpp#L441)
- [`PageLoadState.h#L223`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/PageLoadState.h#L223)
- [`WKPagePrivateMac.h#L45`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/C/mac/WKPagePrivateMac.h#L45)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
