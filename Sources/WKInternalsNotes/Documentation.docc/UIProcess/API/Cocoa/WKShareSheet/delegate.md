# ``WKInternalsNotes/WKShareSheet/delegate``

共有シートの delegate を設定する。

## Objective-C Declaration
```objective-c
@property (nonatomic, weak) id <WKShareSheetDelegate> delegate;
```

## Default Value
`nil`。

## Discussion
共有シートの表示/非表示イベントを受け取る delegate を保持する。

## References
- [`WKShareSheet.h#L49`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/WKShareSheet.h#L49)
- [`WKShareSheet.mm#L243`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/WKShareSheet.mm#L243)
- [`WKShareSheet.mm#L248`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/WKShareSheet.mm#L248)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
