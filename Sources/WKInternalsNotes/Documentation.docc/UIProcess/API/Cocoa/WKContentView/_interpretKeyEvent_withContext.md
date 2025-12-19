# ``WKInternalsNotes/WKContentView/_interpretKeyEvent(_:withContext:)``

キーイベントを解釈し、必要な入力処理を行う。

## Objective-C Declaration
```objective-c
- (BOOL)_interpretKeyEvent:(::WebEvent *)event withContext:(WebKit::KeyEventInterpretationContext&&)context;
```

## Discussion
スクロール用キー処理やシステム入力経路への委譲判定を行い、編集可能な場合は `UIKeyboardImpl` を使って削除・改行・文字入力を処理する。

## References
- [`WKContentViewInteraction.h#L819`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L819)
- [`WKContentViewInteraction.mm#L7747`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L7747)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
