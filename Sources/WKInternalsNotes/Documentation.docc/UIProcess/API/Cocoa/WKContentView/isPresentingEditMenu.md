# ``WKInternalsNotes/WKContentView/isPresentingEditMenu``

編集メニューを表示中かどうかを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) BOOL isPresentingEditMenu;
```

## Default Value
`_isPresentingEditMenu` を返す。

## Discussion
編集メニュー表示の内部フラグ `_isPresentingEditMenu` を返す。

## References
- [`WKContentViewInteraction.h#L587`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L587)
- [`WKContentViewInteraction.mm#L13541`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L13541)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
