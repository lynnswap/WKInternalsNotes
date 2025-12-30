# ``WKInternalsNotes/WKExtrinsicButton/delegate``

コンテキストメニューの表示/終了を通知する delegate。

## Objective-C Declaration
```objective-c
@property (nonatomic, weak) id<WKExtrinsicButtonDelegate> delegate;
```

## Default Value
初期値は `nil`。

## Discussion
`contextMenuInteraction:willDisplayMenuForConfiguration:` と `willEndForConfiguration:` で delegate メソッドを呼び出す。

## References
- [`WKExtrinsicButton.h#L39`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKExtrinsicButton.h#L39)
- [`WKExtrinsicButton.mm#L45`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKExtrinsicButton.mm#L45)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
