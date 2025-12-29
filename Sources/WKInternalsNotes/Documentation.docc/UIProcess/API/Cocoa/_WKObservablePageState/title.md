# ``WKInternalsNotes/_WKObservablePageState/title``

ページのタイトルを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, copy) NSString *title;
```

## Default Value
初期値は `nil`（`PageLoadState` のタイトル未設定時）。

## Discussion
getter は `PageLoadState::title()` を `NSString` 化して返す。`titleFromBrowsingWarning` が設定されている場合はそれを優先する。

## References
- [`WKPagePrivateMac.mm#L86`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/C/mac/WKPagePrivateMac.mm#L86)
- [`PageLoadState.cpp#L364`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/PageLoadState.cpp#L364)
- [`PageLoadState.h#L236`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/PageLoadState.h#L236)
- [`WKPagePrivateMac.h#L43`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/C/mac/WKPagePrivateMac.h#L43)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
