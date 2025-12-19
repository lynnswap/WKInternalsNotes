# ``WKInternalsNotes/WKContentView/_updateInputContextAfterBlurringAndRefocusingElement()``

再フォーカス後の入力コンテキストを更新する。

## Objective-C Declaration
```objective-c
- (void)_updateInputContextAfterBlurringAndRefocusingElement;
```

## Discussion
フォーカス要素があり選択アシスタント抑制中であれば、テキスト入力コンテキストを無効化して再構築を促す。

## References
- [`WKContentViewInteraction.h#L809`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L809)
- [`WKContentViewInteraction.mm#L8687`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L8687)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
